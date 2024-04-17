import re
import html
import csv

#Retrieving links of grant winners announcements (date and link to the page result)
i=1
while i<4: 
  url="https://www.cnc.fr/professionnels/aides-et-financements/resultats-commissions?nomAide=Fonds%20d%27aide%20aux%20cr%C3%A9ateurs%20vid%C3%A9o%20sur%20Internet%20(CNC%20Talent)&_CncPortletRechercheResultatsCommissions_INSTANCE_xLSVbj1jyJkM_cur="+i+"&p_p_id=CncPortletRechercheResultatsCommissions_INSTANCE_xLSVbj1jyJkM&_CncPortletRechercheResultatsCommissions_INSTANCE_xLSVbj1jyJkM_secteur=&_CncPortletRechercheResultatsCommissions_INSTANCE_xLSVbj1jyJkM_annee=&_CncPortletRechercheResultatsCommissions_INSTANCE_xLSVbj1jyJkM_nomAide="
