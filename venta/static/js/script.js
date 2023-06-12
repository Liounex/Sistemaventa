function changeContent(contentId) {
    var contentItems = document.getElementsByClassName('content-item');
    for (var i = 0; i < contentItems.length; i++) {
      contentItems[i].style.display = 'none';
    }
  
    var contentToShow = document.getElementById(contentId);
    contentToShow.style.display = 'block';
  
    var sidebarItems = document.getElementsByClassName('sidebar')[0].getElementsByTagName('li');
    for (var i = 0; i < sidebarItems.length; i++) {
      sidebarItems[i].classList.remove('active');
    }
  
    var clickedItem = document.getElementById(contentId);
    clickedItem.classList.add('active');
  }
  