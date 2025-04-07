document.getElementById("LoginForm").addEventListener("submit", async function (e) {
    console.log("Form submitted"); // Debugging log
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    console.log("Username:", username); // Debugging log
    console.log("Password:", password); // Debugging log

    try {
        const response = await fetch("http://127.0.0.1:5000/Login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json().catch(() => ({ message: "Invalid response from server" }));
        console.log("Response:", data); // Debugging log

        if (response.ok) {
            document.getElementById("errorMessage").textContent = data.message || "Login Successful!";
            document.getElementById("errorMessage").style.color = "green"; 
            document.getElementById("errorMessage").style.display = "block";

            // Redirect to the main page after successful login
            setTimeout(() => {
                window.location.href = "../port/portfolio.html";
            },2000); // 2 seconds delay before redirecting
        } 

        else {
            document.getElementById("errorMessage").textContent = data.message || "Login failed!";
            document.getElementById("errorMessage").style.display = "block";
        }
    } catch (error) {
        document.getElementById("errorMessage").textContent = "An error occurred. Please try again.";
        document.getElementById("errorMessage").style.display = "block";
        console.error("Error:", error); // Debugging log
    }
});
