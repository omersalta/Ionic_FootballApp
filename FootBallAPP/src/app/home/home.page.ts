import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Alert } from 'selenium-webdriver';



export interface User {
  id: number,
  email: string,
  password: string
}


@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})

export class HomePage {

  private users : User[] = [];
  private return_value : number;
  

  constructor(private router: Router, public http   : HttpClient) {
  }


  loadUsers(email:string, password:string) : void
  {
     this.http.get<User[]>('http://localhost/login.php?secret=76f3b1de-7dc4-11e9-8f9e-2a86e4085a59').subscribe(data => {
       this.users = data;
        //console.log(this.users.length)
       let i = 0;
       for (let index = 0; index < this.users.length; index++) {
        // console.log(this.users[index])
         if (this.users[index].email === email && this.users[index].password === password) {
          // console.log(email)
          // console.log(password)
          this.router.navigateByUrl('/main');
          i = 1;
         }
        }
        if (i == 0)
        alert("email or password is incorrect")
        
     });
  }
  
  createUser(email:string, password:string) : void
  {
    this.http.get('http://localhost/signup.php?email='+email+'&password='+password).subscribe(data => {
    });    
    alert("acount created")
  }
  notMatch(){
    alert("Email or Password is incorrect")
  }

  loginAccount() {
    // var empt =  document.getElementsByName("email")[0].nodeValue;
    var email =  document.forms["form1"]["email"].value;
    var pass =  document.forms["form1"]["password"].value;
    if (email != "" && pass != ""){
        this.loadUsers(email, pass);
    }
    else {
      alert('Email or Password could not be empty')
    }
  }

  createAccount() {
    var email =  document.forms["form1"]["email"].value;
    var pass =  document.forms["form1"]["password"].value;
    if (email != "" && pass != ""){
      this.createUser(email, pass);
     
      }else {
        alert('email and password could not be empty')
      }
  }
  
  gostat(){
    this.router.navigateByUrl('/stat');
  }
}

