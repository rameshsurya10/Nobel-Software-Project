document.getElementById("LoginForm").addEventListener("submit", async function(e){
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"  // ✅ Fixed header
        },
        body: JSON.stringify({
            username,password 
        }),
    })
    
    const data = await response.json();  // ✅ Fixed variable declaration
    

    if (data.status === 200) {
        alert("Login successful!");
    }

    else{
        Document.getElementById("errorMessage").textContent = data.message;  // ✅ Fixed variable name and method}
        Document.getElementById("errorMessage").style.display = "block";  // ✅ Fixed variable name and method}
    }
})  
