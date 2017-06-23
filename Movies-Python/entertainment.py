import fresh_tomatoes
import media

logan = media.Movie("Logan","Logan is a 2017 American superhero film featuring the Marvel Comics character Wolverine, played by Hugh Jackman. The film, distributed by 20th Century Fox, is the tenth installment in the X-Men film series, and the third film focused on Wolverine, following X-Men Origins: Wolverine (2009) and The Wolverine (2013)."
                    ,"http://www.beliefnet.com/columnists/moviemom/files/2017/03/logan.jpg"
                    ,"https://www.youtube.com/watch?v=Div0iP65aZo")
#print(logan.poster_image_url)

spiderman = media.Movie("Spider-Man: Homecoming",
                        "Spider-Man: Homecoming is an upcoming American superhero film based on the Marvel Comics character Spider-Man, produced by Columbia Pictures and Marvel Studios, and distributed by Sony Pictures Releasing. It will be the second reboot of the Spider-Man film franchise and the sixteenth film of the Marvel Cinematic Universe (MCU). It will release on 7.7.17 worldwide",
                        "http://orig15.deviantart.net/46ba/f/2016/260/6/a/spider_man_homecoming_by_thedoctor9304-dahwodh.png",
                        "https://www.youtube.com/watch?v=n9DwoQ7HWvI")
#print(spiderman.storyline)

baahubali_2 = media.Movie("Baahubali: 2 The Conclusion",
                          "Baahubali: The Conclusion (English: The One With Strong Arms) is an upcoming Indian epic historical fiction film directed by S. S. Rajamouli. It is the continuation of Baahubali: The Beginning. It will be releasing on 28.4.17 worldwide.",
                          "https://upload.wikimedia.org/wikipedia/en/archive/f/f9/20170312120516%21Baahubali_the_Conclusion.jpg",
                          "https://www.youtube.com/watch?v=YZGSSvsUw14&vl=en")

the_mummy = media.Movie("The Mummy (2017)",
                        "The Mummy is an upcoming American film directed by Alex Kurtzman and written by Jon Spaihts and Christopher McQuarrie. It is a reboot of The Mummy franchise and is intended to be the first installment in the Universal Monsters shared universe. The film stars Tom Cruise, Sofia Boutella, Annabelle Wallis, Jake Johnson, Courtney B. Vance and Russell Crowe. The film is scheduled to be released on June 9, 2017.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/The_Mummy_%282017%29_teaser_poster.jpg",
                        "https://www.youtube.com/watch?v=sCdV3esMr9M")

wonder_woman = media.Movie("Wonder Woman",
                           "Wonder Woman is an upcoming American superhero film based on the DC Comics character of the same name, distributed by Warner Bros. Pictures. It is intended to be the fourth installment in the DC Extended Universe. The Film is scheduled to release on June 2, 2017",
                           "http://images6.fanpop.com/image/photos/39900000/Wonder-Woman-2017-Poster-wonder-woman-2017-39987708-2764-4096.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

justice_league = media.Movie("Justice League",
                             "Justice League is an upcoming American superhero film based on the DC Comics superhero team of the same name, distributed by Warner Bros. Pictures. It is intended to be the fifth installment in the DC Extended Universe. The film is directed by Zack Snyder, with a screenplay by Chris Terrio, from a story by Snyder and Terrio, and features an ensemble cast that includes Ben Affleck, Henry Cavill, Amy Adams, Gal Gadot, Ezra Miller, Jason Momoa, Ray Fisher, Willem Dafoe, Jesse Eisenberg, Jeremy Irons, Diane Lane, Connie Nielsen and J. K. Simmons. In Justice League, Batman and Wonder Woman assemble a team consisting of The Flash, Aquaman, and Cyborg to face the catastrophic threat of Steppenwolf and his army of Parademons.",
                             "https://s-media-cache-ak0.pinimg.com/originals/81/1c/96/811c962100bce08f35cb8901f0bf0677.jpg",
                             "https://www.youtube.com/watch?v=gglkYMGRYlE")

movies = [logan, spiderman, baahubali_2, the_mummy, wonder_woman, justice_league]
fresh_tomatoes.open_movies_page(movies)




