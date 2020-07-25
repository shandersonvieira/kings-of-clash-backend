from pydantic import BaseModel
from typing import List
from .tournament_participant import TournamentParticipant
from .war import War

class Tournament(BaseModel):
    war: War = None
    participants: TournamentParticipant = []
    total_wars: int = 0

    def __repr__(self):
        return '<Tournament {}>'.format(self.war.war_date if self.war else None)

    def add_participant(self, participant):
        try:
            self.participants.append(participant)
        except TypeError:
            self.participants = [participant]

    def get_punishment(self, participant):
        if self.total_wars - participant.matches <= 0:
            return 0
        return self.total_wars - participant.matches

    def get_total(self, participant):
        return participant.collections + participant.bonus - participant.penalties

    def sum(self, other):
        self.war = other.war
        for participant in other.participants:
            tournament_participant = self.get_participant(participant)

            if tournament_participant:
                tournament_participant.collections += participant.collections
                tournament_participant.wars_participated += 1
                tournament_participant.matches += participant.participant.battles_played
                tournament_participant.wins += participant.participant.wins
                tournament_participant.defeats = tournament_participant.matches - tournament_participant.wins
                tournament_participant.bonus = tournament_participant.wins * 300
                tournament_participant.punishment = self.get_punishment(tournament_participant)
                tournament_participant.penalties = tournament_participant.punishment * 500
                tournament_participant.total = self.get_total(tournament_participant)

                try:
                    self.participants.remove(tournament_participant)
                except TypeError:
                    pass
                except ValueError:
                    pass

                self.add_participant(tournament_participant)
            else:
                self.add_participant(participant)

    def get_participant(self, tournament_participant):
        participant = list(filter(lambda x: x.participant.tag == tournament_participant.participant.tag, self.participants))

        if participant:
            return participant[0]
        else:
            return None