from classes.pymongo_uitlezen import Pymongo

pymongo = Pymongo()

pymongo.products(['_id', 'brand', 'category', 'color', 'gender', 'herhaalaankopen',
                  'name', 'price.selling_price', 'properties.doelgroep', 'properties.soort',
                  'properties.variant', 'sub_category', 'sub_sub_category'])

# convert.visitors(['_id', 'buids', 'order.count', 'latest_activity',
#                   'recommendations.segment','recommendations.viewed_before',
#                   'recommendations.similars', 'recommendations.total_pageview_count', 'previously_recommended'])
