import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import ComboBox from "./components/ComboBox";
import data from "./data/iata_codes.json";

function App() { 

  const [formData, setFormData] = useState({
    city_from: "",
    city_to: "",
    date_from: "",
    date_to: "",
    max_days_at_destination: 0,
    currency: "EUR",
    max_flight_prices: 0,
    accept_stopovers: "true", 
  });

  const handleFormChange = (event) => {
    const { name, value } = event.target;
    console.log(`Field ${name} changed for: ${value}`);
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const setCityCode = (code,where)=>{
    const arr = [];
    arr.push(code)
    setFormData(prevState=>{
      return {
        ...prevState,
        [where]: arr
      }
    }); 
  };
  

  const handleSubmit = (event) => {
    event.preventDefault();

    fetch('http://127.0.0.1:5000/submit_form', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Server response:', data);
        // Tutaj możesz dodać logikę obsługi odpowiedzi z serwera
      })
      .catch(error => {
        console.error('Error while sending a request:', error);
        // Tutaj możesz dodać logikę obsługi błędów
      });
  }

  return (
    <div>
        {/*[if lte IE 9]>
            <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
        <![endif]*/}
        {/*welcome-hero start */}
        <section id="home" className="welcome-hero">
          {/* top-area Start */}
          <div className="top-area">
            <div className="header-area">
              {/* Start Navigation */}
              <nav className="navbar navbar-default bootsnav  navbar-sticky navbar-scrollspy" data-minus-value-desktop={70} data-minus-value-mobile={55} data-speed={1000}>
                <div className="container">
                  {/* Start Header Navigation */}
                  <div className="navbar-header">
                    <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#navbar-menu">
                      <i className="fa fa-bars" />
                    </button>
                    <a className="navbar-brand" href="/">Flight Search<span /></a>
                  </div>{/*/.navbar-header*/}
                  {/* End Header Navigation */}
                  {/* Collect the nav links, forms, and other content for toggling */}
                  <div className="collapse navbar-collapse menu-ui-design" id="navbar-menu">
                    <ul className="nav navbar-nav navbar-right" data-in="fadeInDown" data-out="fadeOutUp">
                      <li className="scroll"><a href="/">Home</a></li>
                      <li className="scroll"><a href="/newsletter">Subscription</a></li>
                    </ul>{/*/.nav */}
                  </div>{/* /.navbar-collapse */}
                </div>{/*/.container*/}
              </nav>{/*/nav*/}
              {/* End Navigation */}
            </div>{/*/.header-area*/}
            <div className="clearfix" />
          </div>{/* /.top-area*/}
          {/* top-area End */}
          <div className="container" id="form">
            <div className="row">
              <div className="col-md-12">
                <div className="model-search-content">
                  <form onSubmit={handleSubmit}>
                    <div className="row">
                      <div className="col-md-offset-1 col-md-2 col-sm-12">
                        <div className="single-model-search">
                          <h2>City From:</h2>
                          <div className="model-input">
                              <ComboBox data={data} setCityCode={setCityCode} where="city_from"/>
                          </div>{/* /.model-select-icon */}
                        </div>
                        <div className="single-model-search">
                          <h2>Date From:</h2>
                          <div className="model-select-date">
                            {/*											<select class="form-control">*/}
                            <input style={{padding: '6px 12px'}} type="date" id="date_from" name="date_from" pattern="\d{1,2}/\d{1,2}/\d{4}" onChange={handleFormChange} required />
                            {/*											  	<option value="default">year</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="2018">2018</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="2017">2017</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="2016">2016</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											</select>&lt;!&ndash; /.select&ndash;&gt;*/}
                          </div>{/* /.model-select-icon */}
                        </div>
                      </div>
                      <div className="col-md-offset-1 col-md-2 col-sm-12">
                        <div className="single-model-search">
                          <h2>City To:</h2>
                          <div className="model-input">
                          <ComboBox data={data} setCityCode={setCityCode} where="city_to"/>
                            {/* <input className='form-control' name='city_to' onChange={handleFormChange} required/> */}
                          </div>{/* /.model-select-icon */}
                        </div>
                        <div className="single-model-search">
                          <h2>Date to:</h2>
                          <div className="model-select-date">
                            {/*											<select class="form-control">*/}
                            <input style={{padding: '6px 12px'}} type="date" id="date_to" name="date_to" pattern="\d{1,2}/\d{1,2}/\d{4}" onChange={handleFormChange} required />
                            {/*											  	<option value="default">year</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="2018">2018</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="2017">2017</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="2016">2016</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											</select>&lt;!&ndash; /.select&ndash;&gt;*/}
                          </div>{/* /.model-select-icon */}
                        </div>
                      </div>
                      <div className="col-md-offset-1 col-md-2 col-sm-12">
                        <div className="single-model-search">
                          <h2>Max Days on site:</h2>
                          <div className="model-input">
                            {/*											<select class="form-control">*/}
                            <input type="number" id="max_days_at_destination" name="max_days_at_destination" step={1} min={1}  onChange={handleFormChange} required />
                            {/*											  	<option value="default">make</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="toyota">toyota</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="holden">holden</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="maecedes-benz">maecedes-benz.</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											</select>&lt;!&ndash; /.select&ndash;&gt;*/}
                            {/*										</div>&lt;!&ndash; /.model-select-icon &ndash;&gt;*/}
                          </div>
                        </div>
                        <div className="single-model-search">
                          <h2>Currency:</h2>
                          <div className="model-select-icon">
                            <select className="form-control" name='currency' onChange={handleFormChange}>
                              <option value="EUR">EUR</option>{/* /.option*/}
                              <option value="PLN">PLN</option>{/* /.option*/}
                              <option value="USD">USD</option>{/* /.option*/}
                              <option value="GBP">GBP</option>{/* /.option*/}
                              <option value="JPY">JPY </option>{/* /.option*/}
                            </select>{/* /.select*/}
                          </div>{/* /.model-select-icon */}
                        </div>
                      </div>
                      <div className="col-md-offset-1 col-md-2 col-sm-12">
                        <div className="single-model-search">
                          <h2>Max price for flight:</h2>
                          {/*										<div class="model-select-icon">*/}
                          <div className="model-input">
                            {/*											<select class="form-control">*/}
                            <input type="number" id="max_flight_prices" name="max_flight_prices" min={10} step="1" onChange={handleFormChange} required />
                            {/*											  	<option value="default">make</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="toyota">toyota</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="holden">holden</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											  	<option value="maecedes-benz">maecedes-benz.</option>&lt;!&ndash; /.option&ndash;&gt;*/}
                            {/*											</select>&lt;!&ndash; /.select&ndash;&gt;*/}
                            {/*										</div>&lt;!&ndash; /.model-select-icon &ndash;&gt;*/}
                          </div>
                          <div className="single-model-search">
                            <h2>Accept Stopover:</h2>
                            <div className="model-select-icon">
                              <select className="form-control" name="accept_stopovers" onChange={handleFormChange}>
                                <option value={true}>Yes</option>{/* /.option*/}
                                <option value={false}>No</option>{/* /.option*/}
                              </select>{/* /.select*/}
                            </div>{/* /.model-select-icon */}
                          </div>
                        </div>
                        {/*								<div class="col-md-12 col-sm-12">*/}
                        {/*									<div class="single-model-search text-center">*/}
                        {/*										<button class="welcome-btn model-search-btn" onclick="window.location.href='#'">*/}
                        {/*											search*/}
                        {/*										</button>*/}
                        {/*									</div>*/}
                        {/*								</div>*/}
                      </div>
                      <div className="col-md-12 col-sm-12">
                        <div className="single-model-search text-center">
                          <button className="welcome-btn model-search-btn" type='submit' >
                            search
                          </button>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div className="container">
              <div className="welcome-hero-txt">
                <h2>get your desired flight in resonable price</h2>
                <p>
                  Choose cities, dates and currency to search!
                </p>
                <button className="welcome-btn">Get a subscription!</button>
              </div>
            </div>
          </div></section>{/*/.welcome-hero*/}
        {/*welcome-hero end */}
        <footer id="contact" className="contact">
          <div className="container">
            <div className="footer-top">
              <div className="row">
                <div className="col-md-3 col-sm-6">
                  <div className="single-footer-widget">
                    <div className="footer-logo">
                      <a href="/">Flight Search</a>
                    </div>
                  </div>
                  <p>Authors:</p>
                  <p>Wojciech Marcela</p>
                  <p>Patryk Kurek</p>
                </div>
              </div>
            </div>
            <div className="footer-copyright">
              <div className="row">
                <div className="col-sm-6">

                </div>
                <div className="col-sm-6">
                </div>
              </div>
            </div>{/*/.footer-copyright*/}
          </div>{/*/.container*/}
          <div id="scroll-Top">
            <div className="return-to-top">
              <i className="fa fa-angle-up " id="scroll-top" data-toggle="tooltip" data-placement="top"  data-original-title="Back to Top" aria-hidden="true" />
            </div>
          </div>{/*/.scroll-Top*/}
        </footer>{/*/.contact*/}
        {/*contact end*/}
        {/* Include all js compiled plugins (below), or include individual files as needed */}
        {/*modernizr.min.js*/}
        {/*bootstrap.min.js*/}
        {/* bootsnav js */}
        {/*owl.carousel.js*/}
        {/*Custom JS*/}
      </div>
    );
  }


export default App;
