//! Prompt Fencing Core - Rust implementation for Python SDK.
//!
//! This crate provides the cryptographic foundation for the Prompt Fencing SDK,
//! implementing Ed25519 signing and verification for LLM prompt security boundaries.

pub mod crypto;
pub mod fence;

use pyo3::prelude::*;

/// Python module definition.
/// Module is named `_core` to be imported as `prompt_fencing._core`
#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Fence types
    m.add_class::<fence::FenceType>()?;
    m.add_class::<fence::FenceRating>()?;
    m.add_class::<fence::FenceMetadata>()?;
    m.add_class::<fence::Fence>()?;

    // Crypto functions
    m.add_function(wrap_pyfunction!(crypto::generate_keypair, m)?)?;
    m.add_function(wrap_pyfunction!(crypto::sign_fence, m)?)?;
    m.add_function(wrap_pyfunction!(crypto::verify_fence, m)?)?;
    m.add_function(wrap_pyfunction!(crypto::verify_all_fences, m)?)?;
    m.add_function(wrap_pyfunction!(crypto::build_fenced_prompt, m)?)?;

    // Constants
    m.add("FENCE_AWARENESS_INSTRUCTIONS", crypto::FENCE_AWARENESS_INSTRUCTIONS)?;

    Ok(())
}
