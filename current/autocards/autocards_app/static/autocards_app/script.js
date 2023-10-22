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
            switch(ease) {
                case "1":
                document.getElementById("dif").innerHTML = "Difficulty: Very Hard"
                break
                case 2:
                document.getElementById("dif").innerHTML = "Difficulty: Hard"
                break
                case 3:
                document.getElementById("dif").innerHTML = "Difficulty: Medium"
                break
                case 4:
                document.getElementById("dif").innerHTML = "Difficulty: Easy"
                break
                case 5:
                document.getElementById("dif").innerHTML = "Difficulty: Very Easy"
                break
            }
            console.log(ease)
        }