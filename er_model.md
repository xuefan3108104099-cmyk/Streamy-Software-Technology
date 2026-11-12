# Streamy Entity Relationship Diagram
Relational database schema for Streamy streaming platform.

```mermaid
erDiagram
    USERS {
        int user_id PK
        string username
        string email
        string password_hash
        date join_date
    }

    FILMS {
        int film_id PK
        string title
        int release_year
        int length_minutes
    }

    TV_SHOWS {
        int show_id PK
        string title
        int release_year
        int seasons_count
    }

    SEASONS {
        int season_id PK
        int show_id FK
        int season_number
    }

    EPISODES {
        int episode_id PK
        int season_id FK
        string episode_title
        int duration_minutes
    }

    GENRES {
        int genre_id PK
        string genre_name
    }

    FILM_GENRE {
        int film_id PK,FK
        int genre_id PK,FK
    }

    TVSHOW_GENRE {
        int show_id PK,FK
        int genre_id PK,FK
    }

    REVIEWS {
        int review_id PK
        int user_id FK
        int film_id FK
        int rating_stars
        string review_text
    }

    ACTORS {
        int actor_id PK
        string full_name
    }

    FILM_ACTOR {
        int film_id PK,FK
        int actor_id PK,FK
    }

    TVSHOW_ACTOR {
        int show_id PK,FK
        int actor_id PK,FK
    }

    USERS ||--o{ REVIEWS : writes
    FILMS ||--o{ REVIEWS : receives
    TV_SHOWS ||--o{ SEASONS : contains
    SEASONS ||--o{ EPISODES : contains
    FILMS }|--|{ FILM_GENRE : has
    GENRES }|--|{ FILM_GENRE : maps
    TV_SHOWS }|--|{ TVSHOW_GENRE : has
    GENRES }|--|{ TVSHOW_GENRE : maps
    FILMS }|--|{ FILM_ACTOR : casts
    ACTORS }|--|{ FILM_ACTOR : appears_in
    TV_SHOWS }|--|{ TVSHOW_ACTOR : casts
    ACTORS }|--|{ TVSHOW_ACTOR : appears_in
