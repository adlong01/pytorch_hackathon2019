

$(document).ready(function(){
// your code
  var img = document.createElement("IMG");
  img.src = "monkey.png";
  document.getElementById('div_monkey_img').appendChild(img);

    //BACKGROUND:
    // document.body.style.backgroundColor = "#f3f3f3";
    document.body.style.backgroundColor = "#333333";
    // document.body.style.backgroundImage = "url('img_tree.png')";
    // play_video("videos/0012.mp4");
    // writeDIV();
    // load_videos();
    generate_btn("person");
    get_url_videos();
    load_text("Hi");
    // load_images();
    // load_videos();
    // todaydate();
});



function generate_btn(word){
  
  
  read json
  generate guttons based on List
  write html  buttins to div_json_output
}

function play_video(name_video){
  var vid = document.getElementById(name_video); 

function playVid() { 
    vid.play(); 
} 

function pauseVid() { 
    vid.pause(); 
}
}


function video_gallery(){
  var urls = get_url_videos();
  load_videos(urls, "div_video_gallery");
}

// function load_videos(urls, div_write){

function load_videos(){
    jQuery("#div_video_gallery").nanogallery2({
    items:[
      {
        src:          'https://vimeo.com/32875422',                           // media url
        srct:         'https://i.vimeocdn.com/video/222726041_1280x720.jpg',  // media thumbnail url
        title:        'Vimeo video',                                          // media title
        description:  'Video'                                                 // media description
      },
      { src: 'https://www.youtube.com/watch?v=Ir098VWCv8Q', title: 'Youtube video' },
      { src: 'https://www.dailymotion.com/video/x4wtyl6',   title: 'Dailymotion video' },
      { src: 'berlin1.jpg',      srct: 'berlin1t.jpg',   title: 'Title Image' }
    ],
    thumbnailWidth:  'auto',
    thumbnailHeight: 170,
    itemsBaseURL:    'https://nanogallery2.nanostudio.org/samples/',
    locationHash:    false
  });


}

function get_url_videos() {  
  var pdfFilesDirectory = 'videos/';
  // get auto-generated page 
    var text = "";
$.ajax({url: pdfFilesDirectory}).then(function(html) {
    // create temporary DOM element
    var document = $(html);
    // find all links ending with .pdf 
    document.find('a[href$=".mp4"]').each(function() {
        var pdfName = $(this).text();
        var pdfUrl = $(this).attr('href');
        // console.log(pdfName);
        // console.log(pdfUrl);
        text += pdfName;
        load_text(pdfName);
    })
});
    document.getElementById('div_frame_gallery').innerHTML = "<h1>" + text + "</h1>";
}

  function load_text(var_text){
    var files2 = "load_videos text";  
    var files3 = "Hello2";
    document.getElementById('div_frame_gallery').innerHTML = "<h1>" + var_text + "</h1>";
  }

// function load_videos() {
//   var dir = "../videos/";
// var fileextension = ".mp4";
// $.ajax({
//     //This will retrieve the contents of the folder if the folder is configured as 'browsable'
//     url: dir,
//     success: function (data) {
//         //List all .png file names in the page
//         $(data).find("a:contains(" + fileextension + ")").each(function () {
//             var filename = this.href.replace(window.location.host, "").replace("http://", "");
//             $("div_frame_gallery").append("<img src='" + dir + filename + "'>");
//         });
//     }
// });
// }


function load_images(){
  // var dir = "../img/";
  var dir = "img/";
var fileextension = ".png";
$.ajax({
    //This will retrieve the contents of the folder if the folder is configured as 'browsable'
    url: dir,
    success: function (data) {
        //List all .png file names in the page
        $(data).find("a:contains(" + fileextension + ")").each(function () {
            var filename = this.href.replace(window.location.host, "").replace("http://", "");
            $("div_frame_gallery").append("<img src='" + dir + filename + "'>");
        });
    }
});
}







