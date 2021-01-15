document.addEventListener("DOMContentLoaded", showVideos());

function showVideos() {
  fetch("/videos")
    .then((response) => response.json())
    .then((data) => {
      let elem;
      for (let i in data) {
        switch (data[i].category) {
          case "cars":
            elem = document.querySelector("#cars");
            break;
          case "games":
            elem = document.querySelector("#games");
            break;
          case "programming":
            elem = document.querySelector("#programming");
            break;
          case "tech":
            elem = document.querySelector("#tech");
            break;
        }
        elem.innerHTML += `
        <div class="videos">
        <a href=/video/${data[i].id}><img width="400" height="230" src=${data[i].picture}></a>
        <p class="video"><a href="video/${data[i].id}" class="pre-video">${data[i].title}</a></p>
        </div>`;
      }
    });
}

function upload_video() {
  document.querySelector("#my_videos").style.display = "none";
  document.querySelector("#upload_to_my_videos").style.display = "block";
}

const csrftoken = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};

function searchVideos(text) {
  fetch("/videos")
    .then((response) => response.json())
    .then((data) => {
      data.filter(video => video.title.toLowerCase().includes(text.toLowerCase()))
      window.location.href=`/results/${text}`
    });
}
