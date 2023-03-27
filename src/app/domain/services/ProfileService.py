
from typing import List
from app.domain.model.Profile import Profile


class ProfileService():

    def findAll(self) -> list[Profile]:
        profiles: List = []
        profiles.append(Profile(name='profile1'))
        profiles.append(Profile(name='profile2'))
        return profiles

    def findByProfileId(self, profileId: str):
        pass

profileService = ProfileService()