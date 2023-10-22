var side = false
var ease = 0;
        function flip() {
            if(side) {
                document.getElementById("ty").innerHTML = "Question"
                document.getElementById("qa").innerHTML = cardQ
                document.getElementById("rating").style.display = "none";
                    }
            else {
                document.getElementById("ty").innerHTML = "Answer"
                document.getElementById("qa").innerHTML = cardA
                document.getElementById("rating").style.display = "block";
                }
            side = !side
        }
        function setEase(e) {
            ease = e;
            console.log(ease)
        }