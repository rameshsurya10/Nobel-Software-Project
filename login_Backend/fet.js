document.getElementById("LoginForm").addEventListener("submit", async function (e) {
    console.log("Form submitted"); // Debugging log
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    console.log("Username:", username); // Debugging log
    console.log("Password:", password); // Debugging log

    try {
        const response = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();
        console.log("Response:", data); // Debugging log

        if (response.ok) {
            alert("Login successful!");
            document.getElementById("errorMessage").style.display = "none";
        } else {
            document.getElementById("errorMessage").textContent = data.message || "Login failed!";
            document.getElementById("errorMessage").style.display = "block";
        }
    } catch (error) {
        document.getElementById("errorMessage").textContent = "An error occurred. Please try again.";
        document.getElementById("errorMessage").style.display = "block";
        console.error("Error:", error); // Debugging log
    }
});
