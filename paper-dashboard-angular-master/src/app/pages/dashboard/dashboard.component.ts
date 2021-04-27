import { Component, OnInit } from '@angular/core';
import Chart from 'chart.js';
import {BackendService} from '../../Backend.service';


@Component({
  selector: 'dashboard-cmp',
  moduleId: module.id,
  templateUrl: 'dashboard.component.html'
})

export class DashboardComponent implements OnInit {
  public canvas: any;
  public ctx;
  public chartColor;
  public chartEmail;
  public chartHours;
  selectedOption: any;
  tableHeadings: any;
  rows: any;
  submitButtonFlag:Boolean
  apps:any
  options:any
  redColor: any
  blueColor: any
  memory:any
  condition:any
  conditionArray :[]
  constructor(private backendService: BackendService) {
  }
  ngOnInit() {
    this.memory = 0 +'KB'
    this.selectedOption = "select App"
    this.submitButtonFlag = false
    this.backendService.getMemory().subscribe(data=>{
      console.log(data)
      this.memory = data
    })
    this.condition = false
    this.redColor='#f55d42'
    this.blueColor = 'blue'

    this.rows = []
    this.tableHeadings = []
    this.chartColor = '#FFFFFF';
    this.apps = this.backendService.getApps().subscribe(data=>{
      console.log(data)
      this.options = data
    })


  }

  selectedOption1(option){
    this.selectedOption = option

  }

  updateNow(){
    this.backendService.getMemory().subscribe(data=>{
      console.log(data)
      this.memory = data
    })
  }
  formsubmit(data){
    console.log(data)
    this.backendService.postFilters(data).subscribe(data=>{
      console.log(data)
      let res = []
      for(const data1 in data){
        let temp = []
        this.condition = false
        for(const keys in data[data1]){
          temp.push(data[data1][keys])
          if (data[data1]['text'].toLowerCase().search('error')>=0) {
            this.condition = true
          }
        }
        if(this.condition){
          temp.push(true)
        }
        else{
          temp.push(false)
        }
        res.push(temp)
      }
      this.rows = res
    })
  }
  clicked1() {
    this.submitButtonFlag = true
    console.log(this.selectedOption)
    this.backendService.getLogs(this.selectedOption).subscribe(data=>{
      for (const x in data[0]) {
        console.log(x)
        this.tableHeadings.push(x)
      }
      for (const x in data) {
        let temp = []
        this.condition = false
        for (const xKey in data[x]) {
          temp.push(data[x][xKey])
          if (data[x]['text'].toLowerCase().search('error')>=0) {
            this.condition = true
          }
        }
        if(this.condition){
          temp.push(true)
        }
        else{
          temp.push(false)
        }
        this.rows.push(temp)
      }
    })
    console.log(this.apps)

  }
}
