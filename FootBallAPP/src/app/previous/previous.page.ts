import { Component, OnInit } from '@angular/core';
import { Platform } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { stringify } from '@angular/core/src/render3/util';
import { NavController } from '@ionic/angular';
import { Router } from '@angular/router';

export interface PrevMatch {
  home_team: string,
  away_team: string,
  half_score_0: number,
  half_score_1: number,
  score_0: number,
  score_1: number
}

@Component({
  selector: 'app-previous',
  templateUrl: './previous.page.html',
  styleUrls: ['./previous.page.scss'],
})
export class PreviousPage implements OnInit {

  private home_prev_matches : PrevMatch[]
  private away_prev_matches : PrevMatch[]

  private home_team_half_scores = new Array('a','a','a','a','a','a','a','a','a','a');
  private away_team_half_scores = new Array('a','a','a','a','a','a','a','a','a','a');

  private home_team_second_scores = new Array('a','a','a','a','a','a','a','a','a','a');
  private away_team_second_scores = new Array('a','a','a','a','a','a','a','a','a','a');

  private team_1 : string
  private team_2 : string

  constructor(public plt: Platform, public http   : HttpClient,private navCtrl: NavController,private router: Router) { 
    this.team_1 = plt.getQueryParam("team1")
    this.team_2 = plt.getQueryParam("team2")

    console.log(this.team_1)
    console.log(this.team_2)
  }

  ngOnInit() {
    this.loadHomePrevMatches();
    this.loadAwayPrevMatches();
  }

  loadHomePrevMatches() {

    this.http.get<PrevMatch[]>('http://localhost/prev_matches.php?team=' + this.team_1).subscribe(data => {
      this.home_prev_matches = data;
      

      for (let index = 0; index < this.home_prev_matches.length; index++) {
        let half_score = '';
        half_score = (this.home_prev_matches[index].half_score_0).toString() + '-' 
                + (this.home_prev_matches[index].half_score_1).toString()
        this.home_team_half_scores[index] = (half_score)
        console.log(this.home_team_half_scores[index])
      
        let second_half_score = '';
        second_half_score = (this.home_prev_matches[index].score_0 - this.home_prev_matches[index].half_score_0).toString() + '-' 
                + (this.home_prev_matches[index].score_1 - this.home_prev_matches[index].half_score_1).toString()
        this.home_team_second_scores[index] = (second_half_score)
        console.log(this.home_team_second_scores[index])
      }
    });
  }

  loadAwayPrevMatches() {

    this.http.get<PrevMatch[]>('http://localhost/prev_matches.php?team=' + this.team_2).subscribe(data => {
      this.away_prev_matches = data;
      

      for (let index = 0; index < this.away_prev_matches.length; index++) {
        let half_score = '';
        half_score = (this.away_prev_matches[index].half_score_0).toString() + '-' 
                + (this.away_prev_matches[index].half_score_1).toString()
        this.away_team_half_scores[index] = (half_score)
        console.log(this.away_team_half_scores[index])
      
        let second_half_score = '';
        second_half_score = (this.away_prev_matches[index].score_0 - this.away_prev_matches[index].half_score_0).toString() + '-' 
                + (this.away_prev_matches[index].score_1 - this.away_prev_matches[index].half_score_1).toString()
        this.away_team_second_scores[index] = (second_half_score)
        console.log(this.away_team_second_scores[index])
      }
    });
  }

  Back() {
    this.router.navigateByUrl('/main');
  }

}
