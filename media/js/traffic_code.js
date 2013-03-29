/**
 * Created with PyCharm.
 * User: xp
 * Date: 13-3-26
 * Time: 下午5:18
 * To change this template use File | Settings | File Templates.
 */

var trafficobj={
    "websiteid":"ss"
};

var traffic_start=function(){
    var obj={};
    obj['websiteid']=trafficobj['websiteid'];
    obj['http_referrer']='';
    try{
        obj['http_referrer']=document.referrer;
    }catch (e){}
    if(obj['http_referrer']==''){
        return;
    }
    var url=window.location.href;
    var num1=url.indexOf('/',7);
    var num2=obj['http_referrer'].indexOf('/',7);
    if(url.substring(0,num1)==obj['http_referrer'].substring(0,num2)){
        return ;
    }
    obj['hosturl']=url.substring(0,num1);
    obj['url']=url;
    obj['hostreferrer']=obj['http_referrer'].substring(0,num2);
    obj['referrer']=obj['http_referrer'];
    traffic_send("http://localhost:8005/fromUrl/","POST",obj,function(response){
        alert(response);
    },true);

};
setTimeout(traffic_start,1000);
var traffic_ajax=function (){
       if(window.XMLHttpRequest){
            this.xmlHttp=new XMLHttpRequest();
        }
        else if(window.ActiveXObject){
           try{
               this.xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
           }
           catch(e){
              try{
                this.xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
               }
              catch(e){}
          }
       }
    }
var traffic_send=function (url,method,data,handle,flag){
   url= url ? url : "";
   if(url==""){
   	return;
   }
   flag= flag===false ? false : true;
   method= method ? method : "get";
   data= data ? data : null;
   var xmlHttp=new traffic_ajax();
   var handleResponse= handle ? function(){
   	if(xmlHttp.xmlHttp.readyState==4){
	    if(xmlHttp.xmlHttp.status==200){
	    	//alert(xmlHttp.xmlHttp.responseText);
	    	var o=eval("("+xmlHttp.xmlHttp.responseText+")");
	    	//alert(o.message.message);
	    	handle(xmlHttp.xmlHttp);
	    	//document.getElementById("rightDiv").innerHTML=xmlHttp.xmlHttp.responseText;
	    }
	    else{
	       //alert("您的页面有异常");
	    }
  	}
   } : function(){
   	if(xmlHttp.xmlHttp.readyState==4){
	    if(xmlHttp.xmlHttp.status==200){
	    	//var o=eval("("+xmlHttp.xmlHttp.responseText+")");
	    }
	    else{
	    }
  	}
   };
   xmlHttp.xmlHttp.onreadystatechange=handleResponse;
   xmlHttp.xmlHttp.open(method,url,flag);
   xmlHttp.xmlHttp.setRequestHeader('Content-Type','application/application/json');
   xmlHttp.xmlHttp.setRequestHeader('X-Requested-With','XMLHttpRequest');
   xmlHttp.xmlHttp.send(data);
}

