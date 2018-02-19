$(document).ready(function(){
  var city = "Poltava";
  var searchtext = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "') and u='c'"
  //change city variable dynamically as required
  $.getJSON("https://query.yahooapis.com/v1/public/yql?q=" + searchtext + "&format=json").done(function(data){
   console.log(data);
   $('#temp').html(data.query.results.channel.item.condition.temp+"°C");
  });
});
