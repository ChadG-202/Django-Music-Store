// Only one audio player at a time
$(function(){
    $("audio").on("play", function() {
        $("audio").not(this).each(function(index, audio) {
            audio.pause();
        });
    });
});

// Search button checking
var updateBtns = document.getElementsByClassName('update-search')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var style = this.dataset.style
        updateSearch(style);
    })
}

// Update search based on buttons
function updateSearch(style){
    if (category == undefined){
        category = {'style':style}
    }else{
        category['style'] = style
    }
    document.cookie = 'category=' + JSON.stringify(category) + ";domain=;path=/"
    location.reload()
    const element = document.getElementById("cards");
    element.scrollIntoView();
}

// Search all music
var searchAll = document.getElementsByClassName('nav-link')

for (i = 0; i < searchAll.length; i++) {
    searchAll[i].addEventListener('click', function(){
        resetSearch();
    })
}

function resetSearch(){
    if (category == undefined){
        category = {'style':''}
    }else{
        category['style'] = ''
    }
    document.cookie = 'category=' + JSON.stringify(category) + ";domain=;path=/"
}

// Heart button
var heartBtns = document.getElementsByClassName('heart')

for (i = 0; i < heartBtns.length; i++) {
    heartBtns[i].addEventListener('click', function(){
        var songId = this.dataset.song
        cookieHeartState(songId)
        changeHeartState(songId)
    })
}

function cookieHeartState(songId){
    if (hearted[songId] == undefined){
        hearted[songId] = songId
    }else{
        delete hearted[songId]
    }
    console.log("hearted:", hearted)
    document.cookie = 'hearted=' + JSON.stringify(hearted) + ";domain=;path=/"
    location.reload()
}
