cheet('↑ ↑ ↓ ↓ ← → ← → b a', function () {
    document.getElementById("contactemail").href = "mail" + "to" + ":" + "contact" + "@" + "comfortablynumbered.appspotmail.com";
    var box = document.getElementById('header');
    var can = document.createElement('canvas');
    can.width = box.clientWidth;
    can.height = box.clientHeight;
    box.appendChild(can);
    var ctx = can.getContext('2d');

    function Ball(ctx) {
        this.ctx = ctx;
        this.color = 'hsla(' + Math.floor(360*Math.random()) +', 100%, 50%, 0.5)';
        this.x = Math.random() * this.ctx.canvas.width;
        this.y = -Math.random() * this.ctx.canvas.height;
        this.dx = 2*(Math.random() - 0.5);
        this.dy = 5*(Math.random() - 0.5);
    }
    Ball.prototype.iter = function() {
        this.x += this.dx;
        this.y += this.dy;
        if (this.y > ctx.canvas.height) {
            this.dy *= -1;
        } else {
            this.dy += 0.2;
        }
        if (this.x > ctx.canvas.width + 10 || this.x < -10) {
            this.x = Math.random() * this.ctx.canvas.width;
            this.y = 0;
            this.dx = 2*(Math.random() - 0.5);
            this.dy = 0;
        }
        if (this.y < 0 && Math.random() < 0.8) {
            Ball.call(this, this.ctx);
        }
    };
    Ball.prototype.render = function() {
        this.ctx.fillStyle = this.color;
        this.ctx.beginPath();
        this.ctx.arc(this.x, this.y, 5, 0, Math.PI*2, false);
        this.ctx.fill();
    };

    var balls = [];
    for (var i=0; i<20; i++) {
        balls.push(new Ball(ctx));
    }
    function loop() {
        can.width = box.clientWidth;
        can.height = box.clientHeight;
        balls.forEach(function(b) {
            b.iter();
            b.render();
        });
        (window.requestAnimationFrame       ||
         window.webkitRequestAnimationFrame ||
         window.mozRequestAnimationFrame    ||
         (function(x) {setInterval(x, 1000/60); }))(loop);
    };
    loop();
});
