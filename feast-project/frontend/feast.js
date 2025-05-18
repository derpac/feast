function uploadJson() {
  const fileInput = document.getElementById('jsonFile');
  const file = fileInput.files[0];
  if (!file) return alert('Please choose a file');

  const formData = new FormData();
  formData.append('file', file);

  fetch('http://localhost:5000/upload', {
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
  console.log('Displacements:', displacements);
  const nodes = input.nodes;
  const elements = Object.values(input.elements);
  console.log('nodes', nodes);
  console.log('elements', elements);
}