

document.addEventListener("DOMContentLoaded", () => 
{
    fetch("/api/guestbook")
        .then(raw => raw.json())
        .then(resp => {
            console.log(resp);
        })
        .catch((err) => {
            console.log("did not work!!!");
            console.log(err);
        })

})