from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Library Management System</title>
<style>
  body { font-family: Georgia, serif; text-align: center; margin-top: 80px; background: radial-gradient(circle, #e3f2fd, #bbdefb); color: #1a237e; }
  h1 { color: #0d47a1; animation: slideIn 1.5s ease-in-out; }
  button { background-color: #1976d2; border: none; padding: 10px 20px; color: white; font-weight: bold; cursor: pointer; border-radius: 6px; transition: background-color 0.3s, transform 0.2s; margin: 10px; }
  button:hover { background-color: #0d47a1; transform: scale(1.1); }
  @keyframes slideIn { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
  #section { display: none; margin-top: 20px; padding: 15px; border: 2px solid #0d47a1; border-radius: 10px; background: #e8eaf6; max-width: 500px; margin-left: auto; margin-right: auto; }
</style>
</head>
<body>
  <h1>Library Management System</h1>
  <p>Manage books, members, and borrow records easily!</p>
  <button onclick="showSection('books')">View Available Books</button>
  <button onclick="showSection('members')">View Members</button>
  <button onclick="showSection('borrow')">Borrowed Books</button>
  <div id="section"></div>
<script>
function showSection(type) {
  const section = document.getElementById('section');
  let content = '';
  if (type === 'books') {
    content = `<h3>Available Books</h3>
<ul style="text-align:left;">
<li>The Great Gatsby — F. Scott Fitzgerald</li>
<li>To Kill a Mockingbird — Harper Lee</li>
<li>1984 — George Orwell</li>
<li>Introduction to Algorithms — Cormen</li>
</ul>`;
  } else if (type === 'members') {
    content = `<h3>Registered Members</h3>
<ul style="text-align:left;">
<li>John Doe (ID: 101)</li>
<li>Mary Smith (ID: 102)</li>
<li>Rahul Verma (ID: 103)</li>
</ul>`;
  } else if (type === 'borrow') {
    content = `<h3>Borrowed Books</h3>
<ul style="text-align:left;">
<li>1984 — Borrowed by John Doe (Due: 20 Aug 2025)</li>
<li>The Great Gatsby — Borrowed by Mary Smith (Due: 25 Aug 2025)</li>
</ul>`;
  }
  section.innerHTML = content;
  section.style.display = 'block';
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # listen on all interfaces so container mapping works
    app.run(host='0.0.0.0', port=5000)
