"""Tests for prompt_fence types."""

from prompt_fence.types import FenceRating, FenceSegment, FenceType, VerificationResult


class TestFenceType:
    def test_enum_values(self):
        assert FenceType.INSTRUCTIONS.value == "instructions"
        assert FenceType.CONTENT.value == "content"
        assert FenceType.DATA.value == "data"

    def test_str_enum(self):
        # FenceType is a str enum, value equals the string
        assert FenceType.INSTRUCTIONS == "instructions"
        assert FenceType.INSTRUCTIONS.value == "instructions"
        assert FenceType.CONTENT.value == "content"


class TestFenceRating:
    def test_enum_values(self):
        assert FenceRating.TRUSTED.value == "trusted"
        assert FenceRating.UNTRUSTED.value == "untrusted"
        assert FenceRating.PARTIALLY_TRUSTED.value == "partially-trusted"

    def test_str_enum(self):
        assert FenceRating.TRUSTED == "trusted"


class TestFenceSegment:
    def test_segment_creation(self):
        segment = FenceSegment(
            content="Hello world",
            fence_type=FenceType.INSTRUCTIONS,
            rating=FenceRating.TRUSTED,
            source="test",
            timestamp="2025-01-15T10:00:00.000Z",
            signature="abc123",
            xml="<sec:fence>Hello world</sec:fence>",
        )

        assert segment.content == "Hello world"
        assert segment.fence_type == FenceType.INSTRUCTIONS
        assert segment.rating == FenceRating.TRUSTED
        assert segment.is_trusted
        assert not segment.is_untrusted

    def test_untrusted_segment(self):
        segment = FenceSegment(
            content="User input",
            fence_type=FenceType.CONTENT,
            rating=FenceRating.UNTRUSTED,
            source="user",
            timestamp="2025-01-15T10:00:00.000Z",
            signature="def456",
            xml="<sec:fence>User input</sec:fence>",
        )

        assert segment.is_untrusted
        assert not segment.is_trusted

    def test_str_returns_xml(self):
        segment = FenceSegment(
            content="Test",
            fence_type=FenceType.DATA,
            rating=FenceRating.PARTIALLY_TRUSTED,
            source="api",
            timestamp="2025-01-15T10:00:00.000Z",
            signature="xyz",
            xml="<sec:fence>Test</sec:fence>",
        )

        assert str(segment) == "<sec:fence>Test</sec:fence>"


class TestVerificationResult:
    def test_valid_result(self):
        result = VerificationResult(
            valid=True,
            content="Test content",
            fence_type=FenceType.INSTRUCTIONS,
            rating=FenceRating.TRUSTED,
            source="system",
            timestamp="2025-01-15T10:00:00.000Z",
        )

        assert result.valid
        assert bool(result)
        assert result.content == "Test content"

    def test_invalid_result(self):
        result = VerificationResult(
            valid=False,
            error="Signature verification failed",
        )

        assert not result.valid
        assert not bool(result)
        assert result.error == "Signature verification failed"
