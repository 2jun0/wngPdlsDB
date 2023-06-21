from mongoengine import QuerySet
from wngPdlsDB.document import ArtistDocument, AlbumDocument, TagDocument, SongDocument
from wngPdlsDB.dto import ArtistDto, AlbumDto, TagDto, SongDto
from wngPdlsDB.exception import (
    NotFoundArtistException,
    NotFoundAlbumException,
    NotFoundTagException,
    NotFoundSongException,
)


def _find_artist_doc_by_dto(artist: ArtistDto) -> ArtistDocument:
    artist = ArtistDocument.objects(genie_id=artist.genie_id).first()

    if not artist:
        raise NotFoundArtistException(f"Can't find artist document: {artist}")

    return artist


def _find_album_doc_by_dto(album: AlbumDto) -> AlbumDocument:
    album = AlbumDocument.objects(genie_id=album.genie_id).first()

    if not album:
        raise NotFoundAlbumException(f"Can't find album document: {album}")

    return album


def _find_tag_doc_by_dto(tag: TagDto) -> TagDocument:
    query_set = TagDocument.objects(genie_id=tag.genie_id)

    if not query_set:
        raise NotFoundTagException(f"Can't find tag document: {tag}")

    return query_set.first()


def _find_tag_docs_by_dto(tags: tuple[TagDto]) -> QuerySet:
    tag_genie_ids = [tag.genie_id for tag in tags]
    query_set = TagDocument.objects(genie_id__in=tag_genie_ids)

    if tags and not query_set:
        raise NotFoundTagException(f"Can't find tag documents: {tags}")

    if len(query_set) != len(tags):
        not_found_tags = []
        founds = list(query_set)

        for song in tags:
            if song in founds:
                not_found_tags.append(song)

        raise NotFoundTagException(f"Can't find tag documents: {not_found_tags}")

    return query_set


def _find_song_doc_by_dto(song: SongDto) -> SongDocument:
    query_set = SongDocument.objects(genie_id=song.genie_id)

    if not query_set:
        raise NotFoundSongException(f"Can't find song document: {song}")

    return query_set.first()


def _find_song_docs_by_dto(songs: tuple[SongDto]) -> QuerySet:
    songs_genie_ids = [songs.genie_id for songs in songs]
    query_set = SongDocument.objects(genie_id__in=songs_genie_ids)

    if songs and not query_set:
        raise NotFoundSongException(f"Can't find song documents: {songs}")

    if len(query_set) != len(songs):
        not_found_songs = []
        founds = list(query_set)

        for song in songs:
            if song in founds:
                not_found_songs.append(song)

        raise NotFoundSongException(f"Can't find song documents: {not_found_songs}")

    return query_set
