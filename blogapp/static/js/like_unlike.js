function UnLike_Like(id) {
  fetch("like/" + id + "/", {
    method: "POST",
    post_id: id,
  })
    .then((response) => response.json())
    .then((Like_or_Notlike) => {
      x = document.querySelector(".lc-" + id).innerHTML;
      if (Like_or_Notlike == "Liked") {
        y = parseInt(x) + 1;
      } else {
        y = parseInt(x) - 1;
      }
      document.querySelector(".lc-" + id).innerHTML = y;
    });
}
