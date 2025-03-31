document.getElementById("LoginForm").addEventListener("submit", function(e){
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/Login", {
        method: "POST",
        headers:{
            "constent-type" : "appplication/json"
        },
        body: JSON.stringify({
            username:username,
            password: password
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
