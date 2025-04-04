document.getElementById("LoginForm").addEventListener("submit", function(e){
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"  // ✅ Fixed header
        },
        body: JSON.stringify({
            username: username,  // ✅ Ensure `username` is defined
            password: password   // ✅ Ensure `password` is defined
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // ✅ Log response for debugging
        if (data.login) {
            alert("Login Successful!");
            localStorage.setItem("token", data.token);  // ✅ Store token if needed
        } else {
            alert("Login Failed: " + data.message);
        }
    })
    .catch(error => console.error("Error:", error));
})  
