UPDATE post SET from_ = 'gijs' WHERE LOWER(from_) LIKE '%gijs%';
UPDATE post SET from_ = 'bas' WHERE LOWER(from_) LIKE '%bas%';
UPDATE post SET from_ = 'rob' WHERE LOWER(from_) LIKE '%rob%';
UPDATE post SET from_ = 'guyon' WHERE LOWER(from_) LIKE '%guyon%';
UPDATE post SET from_ = 'rene' WHERE LOWER(from_) LIKE '%rene%';
UPDATE post SET from_ = 'martin' WHERE LOWER(from_) LIKE '%leuring%';
UPDATE post SET from_ = 'casper' WHERE LOWER(from_) LIKE '%casper%';
UPDATE post SET from_ = 'pp' WHERE LOWER(from_) LIKE '%vries%';
delete from post where from_ not in ('gijs', 'bas', 'rob', 'guyon', 'rene', 'martin', 'casper', 'pp');
delete from post where body = '';

-- moet beter -- verwijder dubbele message_ids
delete from post where message_id in (select post.message_id as weg
FROM post
LEFT OUTER JOIN (
   SELECT MIN(id) as RowId, message_id
   FROM post
   GROUP BY message_id
) as KeepRows ON
   post.id = KeepRows.RowId
WHERE
   KeepRows.RowId IS NULL order by post.message_id);
