document.getElementById('fileForm').onsubmit = async function(e) {
    e.preventDefault();
    const file = document.getElementById('fileInput').files[0];
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
};

async function submitScript() {
    const input = document.getElementById('jsonInput').value;
    const res = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: input
    });
    const data = await res.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
}