function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var username = document.getElementById("username").value;
  
    // Εδώ θα πρέπει να γίνει έλεγχος των διαπιστευτηρίων και ανακατεύθυνση στην κύρια σελίδα
    if (email && password && username) {
      window.location.href = "main.html?username=" + encodeURIComponent(username);
    } else {
      alert("Please enter valid credentials.");
    }
  }