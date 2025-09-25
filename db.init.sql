
CREATE TABLE Guests (
    guestID SERIAL PRIMARY KEY,
    fullName VARCHAR(50) NOT NULL,
    comment VARCHAR(100)
)