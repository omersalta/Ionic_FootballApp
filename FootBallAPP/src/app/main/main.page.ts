import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

//import { HttpClientModule, /* other http imports */ } from "@angular/common/http";

export interface Match {
  id: number,
  home_team: string,
  away_team: string
}

export interface Stats {
  homeA0: number,
  homeS0: number,
  homeA1: number,
  homeS1: number,
  awayA0: number,
  awayS0: number,
  awayA1: number,
  awayS1: number
}


@Component({
  selector: 'app-main',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
})
export class MainPage implements OnInit {

  
  private last_week_matches: Match[] = [];
  private stats: Stats[] = [];

  private awayTeamEstHScore: number[]; //they are average of all goals
  private homeTeamEstHScore: number[];
  private awayTeamEstSScore: number[];
  private homeTeamEstSScore: number[];


  private homeTeams: string[]
  private awayTeams: string[]

 
  private homeTeamSTD_0 : number[]
  private homeTeamSTD_1 : number[]

  
  private awayTeamSTD_0 : number[]
  private awayTeamSTD_1 : number[]


  constructor(public navCtrl: NavController,private router: Router,
    public http   : HttpClient) {
    this.stats = new Array();
    this.homeTeams = new Array();
    this.awayTeams = new Array();

    
    this.homeTeamEstHScore = new Array(10.2,10.2,10.2,10.2,10.2,10.2,10.2,10.2,10.2,10.2);
    this.awayTeamEstHScore = new Array(8.3,8.3,8.3,8.3,8.3,10.2,10.2,10.2,10.2,10.2);
    this.homeTeamEstSScore = new Array(10.2,10.2,10.2,10.2,10.2,10.2,10.2,10.2,10.2,10.2);
    this.awayTeamEstSScore = new Array(8.3,8.3,8.3,8.3,8.3,10.2,10.2,10.2,10.2,10.2);

   
    this.homeTeamSTD_0 = new Array(9,9,9,9,9,9,9,9,9,10);
    this.homeTeamSTD_1 = new Array();

    this.awayTeamSTD_0 = new Array();
    this.awayTeamSTD_1 = new Array();
  }

  

  ngOnInit() {
    this.loadMatches();
  }

  Previous(index_str : string)
  {
    console.log(index_str);
    let index = parseInt(index_str);
    this.router.navigateByUrl('/previous' + '?team1=' + this.homeTeams[index] + '&team2=' + this.awayTeams[index]);
  }

  Logout()
  {  console.log("basıldı1");
      this.router.navigateByUrl('/home');
      console.log("basıldı2");
  }



   loadMatches() : void
   {

      this.http.get<Match[]>('http://localhost/last_week.php').subscribe(data => {
        this.last_week_matches = data;
        // console.log(this.last_week_matches.length)

        for (let i = 0; i < this.last_week_matches.length; i++) {
          this.homeTeams[i] = this.last_week_matches[i].home_team
          this.awayTeams[i] = this.last_week_matches[i].away_team

         

          this.http.get<Stats[]>('http://localhost/home_stats.php?HOME='+ this.last_week_matches[i].home_team + '&AWAY='+ this.last_week_matches[i].away_team).subscribe(data => {
            this.stats = data;
            console.log(this.last_week_matches[i].home_team)
            console.log(this.last_week_matches[i].away_team)
              console.log(this.stats[0].homeA0)
              console.log(this.stats[0].homeS0)
              console.log(this.stats[0].homeA1)
              console.log(this.stats[0].homeS1)
    
              this.homeTeamEstHScore[i] = this.stats[0].homeA0;
              this.homeTeamSTD_0[i] = this.stats[0].homeS0;
              this.homeTeamEstSScore[i] = this.stats[0].homeA1;
              this.homeTeamSTD_1[i] = this.stats[0].homeS1;
    
              this.awayTeamEstHScore[i] = this.stats[0].awayA0;
              this.awayTeamSTD_0[i] = this.stats[0].awayS0;
              this.awayTeamEstSScore[i] = this.stats[0].awayA1;
              this.awayTeamSTD_1[i] = this.stats[0].awayS1;
              
    
          });
        }
        
      });
      
   }



   


}
