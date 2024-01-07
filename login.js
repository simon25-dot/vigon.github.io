document.querySelector('form').addEventListener('submit', function(event) {
          event.preventDefault();
          
          var username = document.getElementById('username').value;
          var password = document.getElementById('password').value;
          
          // Replace with your actual login process
          console.log('Username:', username);
          console.log('Password:', password);
      });