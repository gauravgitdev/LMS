var player;
var video_List;

document.onreadystatechange = function() {
  if(document.readystate === "interactive"){

    player = document.getElementById('player');
    video_list = document.getElementById('video_list')
   
    maintainRatio();
  }
}


function maintainRatio() {
    var w = player.clientWidth;
    var h = (w*9) / 16; // 16:9 aspect ratio
    player.height=h;
     video_list.style.maxheight = h + 'px';
  }
  window.onresize = maintainRatio