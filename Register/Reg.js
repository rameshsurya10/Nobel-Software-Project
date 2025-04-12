function displayMessage(message, isSuccess = false) {
    const errorMessageElement = document.getElementById("errorMessage");
    if (errorMessageElement) {
        errorMessageElement.textContent = message;
        errorMessageElement.style.color = isSuccess ? "green" : "red";
        errorMessageElement.style.display = "block";
    } else {
        console.error("Error message element not found!");
    }
}

document.getElementById("signup-form").addEventListener("submit", async function (e) {
    console.log("Form submitted"); // Debugging log
    e.preventDefault();
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const mobileno = document.getElementById("mobileno").value;
    const password = document.getElementById("password").value;
    const con_password = document.getElementById("con_password").value;

    console.log("Username:", username); // Debugging log
    console.log("Email:", email); // Debugging log
    console.log("mobile_No:", mobileno); // Debugging log
    console.log("Password:", password); // Debugging log
    console.log("con_password:", con_password); // Debugging log

    // Password confirmation validation
    if (password !== con_password) {
        displayMessage("Passwords do not match!");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/Register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, email, mobileno, password, con_password }),
        });

        const data = await response.json().catch(() => ({ message: "Invalid response from server" }));
        console.log("Response:", data); // Debugging log

        if (response.ok) {
            displayMessage(data.message || "Registered Successful!!!", true);

            setTimeout(() => {
                window.location.href = "../Login/Login.html"; // Redirect to the login page after successful registration
            },5000); // 5 seconds delay before redirecting
        } else {
            displayMessage(data.message || "Registration failed!");
        }
    } catch (error) {
        displayMessage("An error occurred. Please try again.");
        console.error("Error:", error); // Debugging log
    }
});

