use actix_web::{get, post,App, HttpResponse, HttpServer, Responder, middleware::Logger};

#[get("/")]
async fn health() -> impl Responder {
    HttpResponse::Ok()
}

#[post("/dump")]
async fn dump(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "actix_web=info");
    env_logger::init();
    let port = match std::env::var("PORT") {
        Ok(val) => val.parse::<u16>().unwrap()    ,
        Err(_e) => 3000,
    };
    HttpServer::new(move || {  
        let logger = Logger::default();
        App::new()
        .wrap(logger)
            .service(health)
            .service(dump)
    })
    .bind(("0.0.0.0", port))?
    .run()
    .await



}