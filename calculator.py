from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML form
form_html = """
<!doctype html>
<html>
  <body>
    <h2>Simple Calculator</h2>
    <form action="/calculate" method="post">
      <input type="number" step="any" name="num1" placeholder="First number" required>
      <select name="op">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>
      <input type="number" step="any" name="num2" placeholder="Second number" required>
      <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
      <p>Result: {{ result }}</p>
    {% endif %}
  </body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(form_html, result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    op = request.form['op']
    num2 = float(request.form['num2'])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by Zero"
    else:
        result = "Invalid Operator"

    return render_template_string(form_html, result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6060)


