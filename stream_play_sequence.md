# Streamy Playback Sequence Diagram
This sequence diagram describes the runtime interaction when a user requests to play a Film resource on the Streamy platform.

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant MediaService
    participant Title(Film)
    participant ReviewRepo
    participant Database

    User->>UI: Click play on a Film
    UI->>MediaService: requestPlay(titleId)
    MediaService->>Title(Film): playMedia()
    Title(Film)-->>MediaService: return playable status (True/False)
    MediaService->>ReviewRepo: getReviews(titleId)
    ReviewRepo->>Database: SELECT * FROM review WHERE title_id = ?
    Database-->>ReviewRepo: review list
    ReviewRepo-->>MediaService: reviews
    MediaService-->>UI: stream URL + review data
    UI-->>User: Start video player + show reviews
