def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    summary = {}
    for journal_id in Journal.objects.values_list('id', flat=True):
        journal = Journal.objects.get(id=journal_id)
        publications = journal.publication_set.all()
        total_views = 0
        total_downloads = 0
        for publication in publications:
            hits = publication.hit_set.all()
            for hit in hits:
                if hit.action == Hit.PAGEVIEW:
                    total_views += 1
                else:
                    total_downloads += 1
        summary[journal_id] = (total_views, total_downloads)
    return summary