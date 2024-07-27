from app.utils.enums import ListableEnum


class LifecycleStatusEnum(ListableEnum):
    ready_for_processing = 'ready_for_processing'
    processing = 'processing'
    processed = 'processed'
    processing_error = 'processing_error'
    # TODO: Add more lifecycle statuses based on the any new processing steps