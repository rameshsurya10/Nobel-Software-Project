function displayMessage(message, isSuccess = false) {
    const errorMessageElement = document.getElementById("errorMessage");
    errorMessageElement.textContent = message;
    errorMessageElement.style.color = isSuccess ? "green" : "red";
    errorMessageElement.style.display = "block";
}

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
            displayMessage(data.message || "Login Successful!", true);

            // Redirect to the main page after successful login
            setTimeout(() => {
                window.location.href = "https://nobelsoftware.in/";
            },500); // .5 seconds delay before redirecting
        } 

        else {
            displayMessage(data.message || "Login failed!");
        }
    } catch (error) {
        displayMessage("An error occurred. Please try again.");
        console.error("Error:", error); // Debugging log
    }
});

