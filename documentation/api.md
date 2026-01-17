# API Reference

::: prompt_fence
    options:
      show_root_heading: true
      show_source: true

::: prompt_fence.builder
    options:
      show_root_heading: true
      show_source: true

::: prompt_fence.types
    options:
      show_root_heading: true
      show_source: true

### Exceptions

#### class `prompt_fence.FenceError`

Raised when:
- A fence segment has invalid structure (e.g., malformed XML).
- A fence is missing required attributes.
- Parsing a fence fails completely.

*Note: Signature verification failures usually return `False` (in `validate`) or `valid=False` (in `validate_fence`), rather than raising this error.*

#### class `prompt_fence.CryptoError`

Raised when:
- The provided `private_key` or `public_key` is invalid (e.g., wrong length, not Base64).
- Key generation fails.
- Underlying cryptographic signing or verification encounters a fatal error.

