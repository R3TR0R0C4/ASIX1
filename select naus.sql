/*select naus.nom, tripulants.nom
from naus 
join tripulants on naus.nom = tripulants.nom
join (select nom, MIN(pes) as pesMinim max(pes) as pesMaxim
    from naus
    where viatjants.codi_data between '2024-04-01' and '2024-04-2'
    group by naus.nom) on naus.nom=tripulants.nom
where naus.pes =naus.pesMinim or naus.pes = pesMaxim*/

