'use strict';
(function() {
    window.addEventListener('load', init)

    function init() {
        const outer = MQ.StaticMath(document.getElementById('outer'));
        const inner = MQ.StaticMath(document.getElementById('inner'));
        document.getElementById("submit").addEventListener("click", () => {
            getData(outer, inner);
        });
        document.getElementById('outer').style.visibility = 'visible';
        document.getElementById('inner').style.visibility = 'visible';
        document.getElementById('submit').style.visibility = 'visible';
    }

    function getData(outer, inner) {
        const a = outer.innerFields[0].latex();
        const b = outer.innerFields[1].latex();
        const c = inner.innerFields[0].latex();
        const d = inner.innerFields[1].latex();
        console.log(a + ' ' + b + ' ' + c + ' ' + d);
        $.ajax({
            type:"POST",
            url:"/result",
            data:{
                upper_outer: "" + a,
                lower_outer: "" + b,
                upper_inner: "" + c,
                lower_inner: "" + d
            },
            success:function(response){
                document.getElementById('data').innerHTML = response;
                MQ.StaticMath(document.getElementById('data'));
                document.getElementById('answer').style.visibility = 'visible';
            }
        });
    }
})
();