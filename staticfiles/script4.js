//var start = new Date(2021,8,1);
//var sec = 0
//
//setInterval(function() {
//    total_sec = new Date - start / 1000;
//    total_min = Math.floor(total_sec / 60);
//    hours = Math.floor(total_min / 60);
//    min = total_min % 60;
//    sec = total_sec % 60;
//
//
//    $('#timer').text(hours + 'h ' + min + 'm ' + sec + 'sec');
//}, 1000);

 function get_elapsed_time_string(total_seconds) {
  function pretty_time_string(num) {
    return ( num < 10 ? "0" : "" ) + num;
  }

  var days = Math.floor(total_seconds / 3600 / 24);
  total_seconds = total_seconds % (3600*24);

  var hours = Math.floor(total_seconds / 3600);
  total_seconds = total_seconds % 3600;

  var minutes = Math.floor(total_seconds / 60);
  total_seconds = total_seconds % 60;

  var seconds = Math.floor(total_seconds);

  // Pad the minutes and seconds with leading zeros, if required
  days = pretty_time_string(days);
  hours = pretty_time_string(hours);
  minutes = pretty_time_string(minutes);
  seconds = pretty_time_string(seconds);

  // Compose the string for display
  var currentTimeString = days + 'd ' + hours + ":" + minutes + ":" + seconds;

  return currentTimeString;
}

var start = new Date(2021,7,1);
var date_now = new Date();
var elapsed_seconds = (date_now - start) / 1000;

setInterval(function() {
  elapsed_seconds = elapsed_seconds + 1;
  $('#timer').text(get_elapsed_time_string(elapsed_seconds));
}, 1000);
