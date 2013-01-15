
var day=""; 
var month=""; 
var ampm=""; 
var ampmhour=""; 
var myweekday=""; 
var year=""; 
mydate=new Date(); 
myweekday=mydate.getDay(); 
mymonth=mydate.getMonth()+1; 
myday= mydate.getDate(); 
myyear= mydate.getYear(); 
year=(myyear > 200) ? myyear : 1900 + myyear; 
if(myweekday == 0)
weekday=" \u661f\u671f\u65e5 "; 
else if(myweekday == 1) 
weekday=" \u661f\u671f\u4e00 "; 
else if(myweekday == 2) 
weekday=" \u661f\u671f\u4e8c "; 
else if(myweekday == 3) 
weekday=" \u661f\u671f\u4e09 "; 
else if(myweekday == 4) 
weekday=" \u661f\u671f\u56db "; 
else if(myweekday == 5) 
weekday=" \u661f\u671f\u4e94 "; 
else if(myweekday == 6) 
weekday=" \u661f\u671f\u516d "; 
document.write("<font style='font-size: 12px;'>"+year+"\u5e74"+mymonth+"\u6708"+myday+"\u65e5 "+weekday+"</font>"); 
