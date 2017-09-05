import fresh_tomatoes
import movieclass
captain_underpant = movieclass.Movie("Captain Underpants",
                                     "Story of of 2 good friends whose comic came to life,",
                                     "images/cu.jpg",
                                     "https://www.youtube.com/watch?v=VDm_2m-Hg6c")

fault_in_our_stars = movieclass.Movie("Fault in our Stars",
                                      "About 2 people who had cancer and fell in love",
                                      "images/fios.jpg",
                                      "https://www.youtube.com/watch?v=AuVjGbncgQE")

central_intelligence = movieclass.Movie("Central Intelligence",
                                        "Thriller movie of a 2 high school buddies",
                                        "images/ci.jpg",
                                        "https://www.youtube.com/watch?v=MxEw3elSJ8M")
zootopia = movieclass.Movie("Zootopia",
                            "Story of a female detective determined to prove her worth",
                            "images/zoo.jpeg",
                            "https://www.youtube.com/watch?v=bY73vFGhSVk")

katwe = movieclass.Movie("Queen of Katwe",
                         "story of a girl that learns chess and triumphs despite her background",
                         "images/katwe.jpg",
                         "https://www.youtube.com/watch?v=z4l3-_yub5A")
thethirtythree = movieclass.Movie("The 33",
                                  "Story of 33 miners trapped underground",
                                  "images/33.jpg",
                                  "https://www.youtube.com/watch?v=hOoIBOYqHyw")
movies = [captain_underpant, fault_in_our_stars, central_intelligence, zootopia, katwe, thethirtythree]
fresh_tomatoes.open_movies_page(movies)



