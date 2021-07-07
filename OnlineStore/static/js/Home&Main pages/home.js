class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }

    slideIndex = 0;

    showSlides() {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        }
        this.slideIndex++;
        if (this.slideIndex > slides.length) {this.slideIndex = 1}
        for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[this.slideIndex-1].style.display = "block";
        dots[this.slideIndex-1].className += " active";
        setTimeout(this.showSlides, 2500);
    }


    render() {
        return (
            <>
                <div className="slideshow-container">

                    <div className="mySlides fade">
                        <div className="numbertext">1 / 5</div>
                        <img src="/static/images/img_snow_wide.jpg" style="width:100%"/>
                        <div className="text">Caption Text</div>
                    </div>

                    <div className="mySlides fade">
                        <div className="numbertext">2 / 5</div>
                        <img src="/static/images/img_snow_wide.jpg" style="width:100%"/>
                        <div className="text">Caption Two</div>
                    </div>

                    <div className="mySlides fade">
                        <div className="numbertext">3 / 5</div>
                        <img src="/static/images/img_snow_wide.jpg" style="width:100%"/>
                        <div className="text">Caption Three</div>
                    </div>

                    <div className="mySlides fade">
                        <div className="numbertext">4 / 5</div>
                        <img src="/static/images/img_snow_wide.jpg" style="width:100%"/>
                        <div className="text">Caption Two</div>
                    </div>

                    <div className="mySlides fade">
                        <div className="numbertext">5 / 5</div>
                        <img src="/static/images/img_snow_wide.jpg" style="width:100%"/>
                        <div className="text">Caption Two</div>
                    </div>

                </div>
                <br/>

                <div style="text-align:center">
                    <span className="dot"></span>
                    <span className="dot"></span>
                    <span className="dot"></span>
                    <span className="dot"></span>
                    <span className="dot"></span>
                </div>

            </>
        )
    }
}