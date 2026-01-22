<!DOCTYPE html>
<html>
<head>
    <title>Simple GPA Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        select, button {
            margin: 5px 0;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h2>GPA Calculator</h2>
    <label>Number of Classes:</label>
    <input type="number" id="numClasses" min="1">
    <button onclick="createInputs()">Enter</button>
    <div id="classes"></div>
    <br>
    <button onclick="calculateGPA()">Calculate GPA</button>
    <h3 id="result"></h3>
    <script>
        const points = {
            "AP": {
                "A+": 5.7, "A": 5.3, "A-": 5.0,
                "B+": 4.7, "B": 4.3, "B-": 4.0,
                "C+": 3.7, "C": 3.3, "C-": 3.0,
                "D+": 2.7, "D": 2.3, "D-": 2.0,
                "F": 0
            },
            "HONORS": {
                "A+": 5.2, "A": 4.8, "A-": 4.5,
                "B+": 4.2, "B": 3.8, "B-": 3.5,
                "C+": 3.2, "C": 2.8, "C-": 2.5,
                "D+": 2.2, "D": 1.8, "D-": 1.5,
                "F": 0
            },
            "A LEVEL": { // Key is correct here
                "A+": 4.7, "A": 4.3, "A-": 4.0,
                "B+": 3.7, "B": 3.3, "B-": 3.0,
                "C+": 2.7, "C": 2.3, "C-": 2.0,
                "D+": 1.7, "D": 1.3, "D-": 1.0,
                "F": 0
            }
        };

        function createInputs() {
            const container = document.getElementById("classes");
            container.innerHTML = "";
            const n = document.getElementById("numClasses").value;
            let htmlContent = ''; // Use a temporary variable

            for (let i = 0; i < n; i++) {
                htmlContent += `
                    <p> Class ${i + 1}:
                        <select class="level">
                            <option>AP</option>
                            <option>HONORS</option>
                            <option>A LEVEL</option>
                        </select>
                        <select class="grade">
                            <option>A+</option><option>A</option><option>A-</option>
                            <option>B+</option><option>B</option><option>B-</option>
                            <option>C+</option><option>C</option><option>C-</option>
                            <option>D+</option><option>D</option><option>D-</option>
                            <option>F</option>
                        </select>
                    </p>`;
            }
            container.innerHTML = htmlContent; // Assign once
        }

        function calculateGPA() {
            const levels = document.getElementsByClassName("level");
            const grades = document.getElementsByClassName("grade");
            const resultElement = document.getElementById("result");
            resultElement.innerText = "";
            resultElement.classList.remove("error");

            if (levels.length === 0) {
                resultElement.innerText = "Please enter the number of classes first.";
                resultElement.classList.add("error");
                return;
            }

            let total = 0;
            for (let i = 0; i < levels.length; i++) {
                // This lookup is correct as "A LEVEL" matches the option value
                total += points[levels[i].value][grades[i].value];
            }

            const gpa = total / levels.length;
            resultElement.innerText = "Your GPA is: " + gpa.toFixed(2);
        }
    </script>
</body>
</html>
