import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

export interface Team {
  id: number,
  name: string,
  played_games: number
  wins: number
  draws: number
  losses: number
  goals: number
}

// http://localhost/Teams_order_name.php

@Component({
  selector: 'app-stat',
  templateUrl: './stat.page.html',
  styleUrls: ['./stat.page.scss'],
})


export class StatPage implements OnInit {

  private TeamsName : Team [] 
  private TeamNames : string [] 
  private Statistics : string [] 

  constructor(public http : HttpClient,public navCtrl: NavController,private router: Router) {

    this.TeamsName = new Array()
    this.TeamNames = new Array()
    this.Statistics = new Array ("number of corners","number of attacks","number of cards","number of shoots","number of fouls","specials note")
   }


  ngOnInit() {
    this.loadTeamNames();
  }

  loadTeamNames() : void
  {

     this.http.get<Team[]>('http://localhost/home_stats.php').subscribe(data => {
       this.TeamsName = data;
       
       for (let i = 0; i < this.TeamsName.length; i++) {
        this.TeamNames[i] = this.TeamsName[i].name //TeamNames arrayine <--- Team yapısı şeklinde gelen TeamsName arrayinden aktarılması
        //console.log(this.TeamNames[i])
       }

     });
   
  }
  loadStat():void {
    


  }







  compareWithFn = (o1, o2) => {
    return o1 && o2 ? o1.id === o2.id : o1 === o2;
  };

  compareWith = this.TeamNames;

}
