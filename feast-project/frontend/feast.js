function uploadJson() {
  const fileInput = document.getElementById('jsonFile');
  const file = fileInput.files[0];
  if (!file) return alert('Please choose a file');

  const formData = new FormData();
  formData.append('file', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    const reader = new FileReader();
    reader.onload = function(event) {
      const input = JSON.parse(event.target.result);
      drawDeformation(input, data.displacements);
    };
    reader.readAsText(file);
  })
  .catch(err => console.error('Error:', err));
}
  
  function drawDeformation(input, displacements) {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  
    const nodes = input.nodes;
    const elements = Object.values(input.elements);
    const scale = 10000;  // adjust
  
    function map(x, y) {
      return [250 + x * 100, 400 - y * 100]; // canvas transform
    }
  
    // draw undeformed structure (gray)
    ctx.strokeStyle = '#ccc';
    ctx.lineWidth = 1;
    elements.forEach(e => {
      const [n1, n2] = e.nodes.map(n => nodes[n.toString()]);
      const [x1, y1] = map(n1[0], n1[1]);
      const [x2, y2] = map(n2[0], n2[1]);
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();
    });
  
    // draw deformed structure (blue)
    ctx.strokeStyle = 'blue';
    ctx.lineWidth = 2;
    elements.forEach(e => {
      const [n1, n2] = e.nodes;
      const u1 = displacements[n1.toString()];
      const u2 = displacements[n2.toString()];
      const n1_coords = nodes[n1.toString()];
      const n2_coords = nodes[n2.toString()];
  
      const [x1, y1] = map(n1_coords[0] + u1[0] * scale, n1_coords[1] + u1[1] * scale);
      const [x2, y2] = map(n2_coords[0] + u2[0] * scale, n2_coords[1] + u2[1] * scale);
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();
    });
  }